# Web Audio Spectrometer Visualizer
## Objective 
The purpose of the  process_audio  function is to process an audio file by computing its short-time Fourier transform (STFT), generating a magnitude spectrogram plot, and saving the plot to a memory buffer. 
 
## Inputs 
-  filename : A string representing the path to the audio file to be processed. 
 
## Flow 
1. Load the audio file using the  librosa.load()  function and assign the audio signal and sampling rate to  y  and  sr  variables, respectively. 
2. Compute the STFT of the audio signal using the  librosa.stft()  function and assign it to the  stft  variable. 
3. Compute the magnitude spectrogram of the STFT using the  librosa.amplitude_to_db()  function and assign it to the  spectrogram  variable. 
4. Plot the magnitude spectrogram using the  librosa.display.specshow()  function and customize the plot using  matplotlib.pyplot  functions. 
5. Save the plot to a memory buffer using the  plt.savefig()  function and format it as a PNG image. 
6. Return the memory buffer containing the PNG image. 
 
## Outputs 
-  img_buf : A memory buffer containing the PNG image of the magnitude spectrogram plot. 
 
## Additional Aspects 
- The function uses the Flask web framework to run a web application that can process audio files. 
- The  process_audio  function can be used as a part of a larger web application that requires audio processing capabilities. 
- The function can be modified to customize the plot and the format of the output image.