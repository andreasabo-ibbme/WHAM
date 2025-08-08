x=0

# Continue to try processing while the back up file exists
while [[ $x -le 0 ]]
do
    python demo_for_pipeline_with_fps.py
    x=$(( $x + 1 ))
done

