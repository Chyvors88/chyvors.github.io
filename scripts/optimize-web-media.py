"""Export smaller web previews; keep every original/enlarged image unchanged."""
from pathlib import Path
from PIL import Image, ImageOps
import json,re,concurrent.futures
root=Path(__file__).resolve().parents[1]/'docs'
out=root/'assets/delivery';out.mkdir(exist_ok=True)
paths=[]
for folder in ['portfolio','portfolio-enhanced','themes','corporate-themes','mockups']:
 paths.extend(p for p in (root/'assets'/folder).glob('*') if p.suffix.lower() in ['.jpg','.png'] and '-thumb' not in p.stem)
paths.extend(root/'assets'/name for name in ['process-poster.jpg','personal-event-poster.jpg','corporate-event-poster.jpg','creative-studio.jpg'])
def export(p):
 im=ImageOps.exif_transpose(Image.open(p)).convert('RGB');key=str(p.relative_to(root));stem=p.parent.name+'-'+p.stem
 variants=[]
 for size in [480,960]:
  resized=im.copy();resized.thumbnail((size,size),Image.Resampling.LANCZOS);dest=out/(stem+'-'+str(size)+'.webp');resized.save(dest,'WEBP',quality=82,method=6)
  variants.append([str(dest.relative_to(root)),resized.width])
 return key,{'small':variants[0][0],'large':variants[1][0],'smallWidth':variants[0][1],'largeWidth':variants[1][1],'width':im.width,'height':im.height}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex: media=dict(ex.map(export,paths))
for key,value in list(media.items()):
 p=root/key;thumb=p.with_name(p.stem+'-thumb.jpg')
 if thumb.exists():media[str(thumb.relative_to(root))]=value
(root/'media-data.js').write_text('window.backdroppedMedia='+json.dumps(media,separators=(',',':'))+';\n')
# Render each existing logo frame to a small native image, avoiding nested SVG image loading.
p=root/'index.html';html=p.read_text()
def logo(match):
 tile=match[0];name=re.search(r'<span class="client-name">(.*?)</span>',tile)[1];frame=re.search(r'<span class="client-logo-frame([^"]*)">(.*?)</span>',tile,re.S);visual=frame[2]
 src=re.search(r'(?:src|href)="([^"]+)"',visual)[1];source=root/src
 if src.startswith('assets/delivery/'): return tile
 if source.suffix=='.svg':return tile.replace('loading="lazy"','loading="eager"')
 im=Image.open(source).convert('RGBA');box=re.search(r'viewBox="([^"]+)"',visual)
 if box:
  x,y,w,h=map(float,box[1].split());im=im.crop((round(x),round(y),round(x+w),round(y+h)))
 elif 'logo-wide-square' in visual:
  # Match the current centre-cropped CSS frame, preserving the visible logo artwork.
  frame_ratio=160/57;h=min(im.height,round(im.width/frame_ratio));top=(im.height-h)//2;im=im.crop((0,top,im.width,top+h))
 im.thumbnail((480,180),Image.Resampling.LANCZOS);dest=out/('logo-'+source.stem+'.webp');im.save(dest,'WEBP',quality=96,method=6)
 classes=frame[1];new='<span class="client-logo-frame'+classes+'"><img src="'+str(dest.relative_to(root))+'" alt="'+name+' logo" width="'+str(im.width)+'" height="'+str(im.height)+'" loading="eager" decoding="async"></span>'
 return tile.replace(frame[0],new)
html=re.sub(r'<a class="client-tile".*?</a>',logo,html,flags=re.S);p.write_text(html)
# The main logo is displayed at ~200px, not at its 1660px source resolution.
p=root/'assets/brand/backdropped-ocean-blue-spaced.png';im=Image.open(p);im.thumbnail((600,600),Image.Resampling.LANCZOS);im.save(out/'backdropped-logo.webp','WEBP',quality=94,method=6)
for p in root.glob('*.html'):
 s=p.read_text().replace('assets/brand/backdropped-ocean-blue-spaced.png','assets/delivery/backdropped-logo.webp')
 for key,value in media.items():
  s=s.replace('poster="'+key+'"','poster="'+value['large']+'"')
  s=s.replace('src="'+key+'"','src="'+value['large']+'" srcset="'+value['small']+' '+str(value['smallWidth'])+'w, '+value['large']+' '+str(value['largeWidth'])+'w" sizes="(max-width: 760px) 92vw, 50vw"')
 if 'media.js?v=20261014-mobile' not in s: s=s.replace('<script src="corporate-themes.js','<script src="media-data.js?v=20261014-mobile" defer></script><script src="media.js?v=20261014-mobile" defer></script><script src="corporate-themes.js')
 s=s.replace('app.js?v=20261014-exhibition','app.js?v=20261014-mobile').replace('themes.js?v=20261014-exhibition','themes.js?v=20261014-mobile').replace('portfolio.js?v=20261014"','portfolio.js?v=20261014-mobile"')
 # Browser must select the appropriate video before any original desktop source starts fetching.
 s=s.replace('preload="auto"','preload="metadata"').replace('<source src="assets/backdrop-process-smooth.mp4"','<source data-src="assets/backdrop-process-smooth.mp4"').replace('<source src="assets/personal-event-loop-smooth.mp4"','<source data-src="assets/personal-event-loop-smooth.mp4"')
 p.write_text(s)
p=root/'pages.css';s=p.read_text().replace("assets/creative-studio.jpg",media['assets/creative-studio.jpg']['large']);p.write_text(s)
print('Exported',len(paths),'image sources; responsive preview map:',len(media),'entries')
print('Original photo bytes:',sum(p.stat().st_size for p in paths),'Delivery bytes:',sum(p.stat().st_size for p in out.glob('*.webp')))
