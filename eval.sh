echo "Eval ${1}/${2}"
echo "default"
python eval.py OutputImages/default/${1} GroundTruth/${2}
echo "grad_1.5"
python eval.py OutputImages/grad_1.5/${1} GroundTruth/${2}
echo "grad_2.5"
python eval.py OutputImages/grad_2.5/${1} GroundTruth/${2}
echo "low_4"
python eval.py OutputImages/low_4/${1} GroundTruth/${2}
echo "low_16"
python eval.py OutputImages/low_16/${1} GroundTruth/${2}
echo "high_0.25"
python eval.py OutputImages/high_0.25/${1} GroundTruth/${2}
echo "high_0.5"
python eval.py OutputImages/high_0.5/${1} GroundTruth/${2}