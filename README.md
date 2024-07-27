# conv_img 
## Yet another CLI utility to batch convert image files

This one depends on Pillow in Python. 

Unlike other tools, conv_img preserves directories:
	source/tiff/example.tif -> JPG/source/tiff/example.jpg

Parameters
```
USAGE:
	conv_img    # shows what would be done (using defaults)
	conv_img -a # actually do it 
	conv_img -f **/*.jpg # change the filemask how files discovered
	conv_img -t .png     # change destination file format
	conv_img -m 7000     # change the max size of longest side to which image is reduced 
```

