# conv_img 
## Yet another CLI utility to batch convert image files

This one depends on Pillow in Python. 

Unlike other tools, conv_img preserves parts of the path, so we're not converting
images in place (in the same directory as orginal) by default. Also note that we're 
acting on current directory:
```
conv_img DIR
# source/example.tif -> DIR/source/example.jpg
```
## Install
```
git clone https://github.com/mokko/conv_img.git
cd conv_img
pip install .
```


## Usage
```
conv_img [-h] [-a] [-f FILEMASK] [-l LIMIT] [-m MAX_SIZE] [-t TARGET_SUFFIX] [-v] dest_dir

positional arguments:
  dest_dir              destination directory to write to

options:
  -h, --help            show this help message and exit
  -a, --act             carry out conversion instead of just showing what would have been
  -f FILEMASK, --filemask FILEMASK
                        the filemask that identifies which images will be converted, defaults to '**/*.tif'
  -l LIMIT, --limit LIMIT
                        number of images after which script breaks off, defaults to -1 (no limit)
  -m MAX_SIZE, --max_size MAX_SIZE
                        max size of pixel, defaults to 6000 pixel for the longest size
  -t TARGET_SUFFIX, --target_suffix TARGET_SUFFIX
                        target image format, defaults to '.jpg'
  -v, --verbose         more verbose output
```

## More Examples
```
conv_img DIR             # shows what would be done (using defaults)
conv_img -a DIR          # actually do it 
conv_img -f **/*.jpg DIR # the filemask for identifying image
conv_img -t .png DIR     # destination file format; note the period
conv_img -m 7000 DIR     # max size of longest side in pixels that bigger images are reduced
conv_img %               # put new image in original folder (convert in place)
```
