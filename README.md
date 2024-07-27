# conv_img 
## Yet another CLI utility to batch convert image files

This one depends on Pillow in Python. 

Unlike other tools, conv_img preserves directories:
```
	source/tiff/example.tif -> JPG/source/tiff/example.jpg
```

Acts on current directory.

```
USAGE:
	conv_img    # shows what would be done (using defaults)
	conv_img -a # actually do it 
	conv_img -f **/*.jpg # the filemask for identifying image
	conv_img -t .png     # destination file format; note the period
	conv_img -m 7000     # max size of longest side in pixels that bigger images are reduced
```

