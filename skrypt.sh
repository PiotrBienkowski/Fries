for i in {1..350}; do
 
    echo generate $i;
 
    echo $i|python3 gen2.py

    echo $i|python3 svgToPng.py
 
    echo $i|python3 svgToPdf.py
done;
