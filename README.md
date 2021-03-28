# generate-sec-dataset
  
Generate space error correction (SEC) dataset.
  
## Example
  
- Input sentence
```
My dream is to make artificial intelligence like Jarvis in the movie Iron Man
```
- Generate sentence
```
My dre am isto make art i ficialintelligencel ike Jarvis in the movi eIron Man 
```
  
## Usage
  
```
$ python3 main.py --filepath data/example.txt --generate_filepath data/generated.txt
```
  
## Output

- generated.txt
  
|Inputs|Targets|  
|:----:|:-----:|  
|Welooking fortalented  colleagues  towork with.|We looking for talented colleagues to work with. |  
|My d reamistoma k ear tificialintelligence like Jarvisin the movie Ir onMan|My dream is to make artificial intelligence like Jarvis in the movie Iron Man|  
|Ifyouare interested,ple ase don't hesitateto contact me.|If you are interested, please don't hesitate to contact me.|  
  
## Author
  
* Soohwan Kim [@sooftware](https://github.com/sooftware)
* Contacts: sh951011@gmail.com
