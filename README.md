# oxford hack 2020
https://ache17.github.io/oxford_hack/<br>
in 36 hour hackathon we created an chrome extension that communicates with external REST api with GPU that runs deep learning model ( image captioning model).
The model takes the website on which the extension is run, extract images from it and run the deep learning model for images ( model creates a captions/short descriptions for images). Chrome extension then, replace all alt properties for html images with this short description.
<br><br>
__currently it points out to external server with API ( we are using 1 model which perforamance is not great, model 2 is much more sophisticated although we don't have droplet with enough resources )__
<br><br>
model credit:
- https://arxiv.org/pdf/1707.07998v3.pdf
- https://github.com/ruotianluo/ImageCaptioning.pytorch
