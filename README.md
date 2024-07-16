download using ** git clone https://github.com/dan4in/Stable-diffusion-Prompt-Helper-Pony.git 

or downloading zip from releases page  

Make sure to install requirements

launch using start.bat after install/extraction

have fun exploring tags/prompts with interesting/weird combinations to use with pony or other models

**Things working on 
1.  ✅Adding more tags 100%done
2.  ✅Adding characters only suggestion's
3.  ✅seperating Tags SFW/NSFW in a special toggle/button 99% done
5.  ✅Fully offline
6.  ✅Adding seperate categories 99% done
7.  ✅Sending to webui TXT2Image or image2image 100% Done - A1111 or Forge Extension v2.0.0 Found here in its own repository https://github.com/dan4in/PonyHelper


![Charakter_Cicero-4013416703](https://github.com/dan4in/Stable-diffusion-Prompt-Helper-Pony/assets/53431991/9e4d0d3a-8169-4dc5-955f-5c1132a7c36f)


https://github.com/dan4in/Stable-diffusion-Prompt-Helper-Pony/assets/53431991/5de518e5-20c8-42b7-92de-8d82ac6289f2



video https://youtu.be/5jxlOfHOy0M
 

### Adding Custom Data

To add your own data and tags, follow these steps:

1. **Create Your Data File**:
   - Create a text file with your tags, each on a new line.
   - Name the file `YourDATA.txt` (replace `YourDATA` with your desired name).
   - Remove the `.txt` extension after you’re done.

2. **Modify the Script**:
   - Open `Ponygenerator.py` and add the following lines to read your new tags:
Line 48
     ```python
     # Read tags from the text files
     tags = {
         'YourDATA': read_tags_from_file('YourDATA'),
     }
     ```

3. **Update the HTML**:
   - In `example.html`, add a new line at line 155:

     ```html
     <option value="YourDATA">YourDATA</option>
     ```

   - Add a new section at line 269:

     ```html
     <div class="checkbox-group">
         <input type="checkbox" id="mixed-YourDATA" name="mixed-YourDATA">
         <label for="mixed-YourDATA">YourDATA</label>
         <input type="range" id="YourDATA-slider" name="YourDATA-slider" min="1" max="15" value="1">
     </div>
     ```

4. **Update the JavaScript**:
   - In your JavaScript file, add a new line at line 429:

     ```javascript
     mixedTagsOptions['YourDATA'] = $('#mixed-YourDATA').is(":checked") ? $('#YourDATA-slider').val() : 0;
     ```



previews:
   
score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, nontraditional_miko, against_wall, kongou_(kancolle), dark_skin, black_nails, silk, rating_safe
![00037-1171490274](https://github.com/dan4in/Random-Danbooru-Tags-Generator-Pony/assets/53431991/415b402e-f2b1-426e-9560-78f6148f220f)

3D CG ART: A realistic and detailed image of a minimalist house in 3D and 2D, designed in a style inspired by four-leaf clovers. The house is situated on the edge of a river, where an impressive waterfall flows in three shades of blue, indigo and green. The landscape in the background presents a combination of warm and fresh tones, creating an atmosphere of harmony and balance. The 15000K resolution captures the texture and reality of the environment, inviting the viewer to explore this unique and
![00104-3505023787](https://github.com/dan4in/Stable-diffusion-Prompt-Helper-Pony/assets/53431991/8de6d450-26b9-4006-bb1e-1bfbe08fd7b2)

.
.
.
.
score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, ambiguous_gender, dog_tail, singing, yellow_fur, eiyuu_densetsu, rating_safe
![00045-782946285](https://github.com/dan4in/Random-Danbooru-Tags-Generator-Pony/assets/53431991/045a3229-beb1-4fd1-82a0-e563c41982ea)
.
.
.
.
.

score_10,score_9_up,score_8_up,score_7_up, score_9, score_8_up, score_7_up, score_6_up, score_5_up, score_4_up, jeweled_branch_of_hourai, cable_knit, elira_pendora, clip_studio_paint_(medium), feather_hair, beer_can, dragon_tail, kashiwazaki_sena, pectorals, rating_safe
![00042-2995763453](https://github.com/dan4in/Random-Danbooru-Tags-Generator-Pony/assets/53431991/03da876b-cb82-4e7d-b55c-911ab4eed185)
.
.
.

![image](https://github.com/dan4in/Random-Danbooru-Tags-Generator-Pony/assets/53431991/4ece34b2-3b05-4d1d-8183-cf40175260e8)
![c1b7dc14-1115-47e1-b60f-406a8d95ddc3](https://github.com/dan4in/Stable-diffusion-Prompt-Helper-Pony/assets/53431991/d13aece9-5929-4545-8da0-2eedb419ecf4)

