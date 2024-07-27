# conv_img 
## Yet another CLI utility to batch convert image files

This one depends on Pillow in Python. 

Unlike other tools, conv_img preserves directories:
```
	conv_img DIR
	# source/tiff/example.tif -> DIR/source/tiff/example.jpg
```

Acts on current directory.

```
USAGE:
	conv_img DIR             # shows what would be done (using defaults)
	conv_img -a DIR          # actually do it 
	conv_img -f **/*.jpg DIR # the filemask for identifying image
	conv_img -t .png DIR     # destination file format; note the period
	conv_img -m 7000 DIR     # max size of longest side in pixels that bigger images are reduced
```

