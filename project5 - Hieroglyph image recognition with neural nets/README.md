Hi guys! 

Glad you made it here. You are looking at my very first neural network project: Egyptian Hieroglyph Recognition with Neural Network. The backend model is trained in two steps with convolutional variational autoencoder (C-VAE) to obtain latent features, and then with artificial neural network (ANN) dense layers as an image classifier. The API frontend is coded in Python Flask.

Feel free to also take a look at [my presentation slide desk](./Hieroglyph_Huang06292017.pdf) and [my app demo posted on YouTube](https://www.youtube.com/watch?v=LChIxAN2jVM).

Unfortunately the api result is currently hardcoded. The model itself works well locally, but the size is too large for it to be uploaded onto herokuapp.com where the api is served - even after pickling. I am all ears if there are any tips or tricks around this that you are willing to share!

Cheers,  
Katie
