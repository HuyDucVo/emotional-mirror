# Emotional Mirror Interface
 Every day, we use a mirror to comb our hair or makeup. However, the mirror is emotional-less. A lot of people feel discouraged or even don't want to look at the mirror. We all know appearance is very important, but confidence is more important. 


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
<img src="/images/happy.png" width="500px>
Output
<img src="/sample_output/output_image_INT8.jpg" width="500px>

+ **Video:**
Input
<img src="/doc/video_input.gif">
Output
<img src="/sample_output/prototype_INT8.gif" width="500px">

## Reference
Doraemon Anime
[MDI Management Development International](https://www.youtube.com/watch?v=embYkODkzcs)



*Intel® Edge AI Scholarship Program Project Showcase*
