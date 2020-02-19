# Emotional Mirror Interface
 Every day, we use a mirror to comb our hair or makeup. However, the mirror is emotional-less. Many people feel discouraged or even don't want to look at the mirror. We all know appearance is very important, but confidence is more important. With the right words and sentences at the right moment and feelings, we can bring a whole new UX to the users. 


**Emotional Mirror Interface provides an interface connecting user's emotion to other applications like Google Voice, Siri, Youtube, etc to advance the User Experience of the mirror.**
 
<img src="/doc/intro_reduced.gif">

## Installation
1. Follow [Intel® Distribution of OpenVINO™ Toolkit](https://software.intel.com/en-us/openvino-toolkit/choose-download)

2. Install (Recommend) [Jupyterlab](https://jupyterlab.readthedocs.io/en/stable/getting_started/overview.html)

3. Clone this repo

## Usage

**Argument Structure**
<img src="/doc/args.png">

*Note: there are a few models and input in /models /images /videos for you to try out*

Here are some sample usage: 
+ **For Image:**
<img src="/doc/image.gif">

```
python app.py -m model/INT8/emotions-recognition-retail-0003.xml -i images/happy.png -t IMAGE
```

+ **For Video:**
<img src="/doc/video.gif">

```
python app.py -m model/INT8/emotions-recognition-retail-0003.xml -i videos/faces.mp4 -t VIDEO
```

## Output
+ **Image:**

Input  
<img src="/images/happy.png" width="500px">  
Output  
<img src="/sample_output/output_image_INT8.jpg" width="500px">  

+ **Video:**

Input  
<img src="/doc/video_input.gif">  
Output  
<img src="/sample_output/prototype_INT8.gif" width="500px">  
## Techniques
[x] Intel Model Zoo
[x] Handling Network Output


## Reference
[Doraemon Anime](https://www.youtube.com/watch?v=MC2oUNPzU3I)

[MDI Management Development International](https://www.youtube.com/watch?v=embYkODkzcs)

[OpenVINO Toolkit](https://docs.openvinotoolkit.org/latest/_models_intel_emotions_recognition_retail_0003_description_emotions_recognition_retail_0003.html)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to test as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)

*Intel® Edge AI Scholarship Program Project Showcase* 
<br>
<img src="/doc/certificate-participant-bleed-1200x900.jpg" width="500px"> 

