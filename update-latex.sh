# copy files from data
DATA=data
LATEX=net-flow-opt-latex

cp $DATA/continuous_r*.csv $LATEX/$DATA
cp $DATA/discrete_r*.csv $LATEX/$DATA

cp $DATA/continuous_hv_r*.csv $LATEX/$DATA
cp $DATA/discrete_hv_r*.csv $LATEX/$DATA

# update repo
cd $LATEX
git add $DATA
git commit -m "Updated data."
git push
cd ..
