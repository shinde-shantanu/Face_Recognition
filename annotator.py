from pigeon import annotate
from IPython.display import display, Image

annotations = annotate(
  ['assets/img_example1.jpg', 'assets/img_example2.jpg'],
  options=['shantanu', 'prutha'],
  display_fn=lambda filename: display(Image(filename))
)