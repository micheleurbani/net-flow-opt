# copy files from data
DATA=data
LATEX=net-flow-opt-latex

algorithms=(continuous discrete hybrid)

for al in "$algorithms[@]"; do
    cp $DATA/$al_r*.csv $LATEX/$DATA
    cp $DATA/$al_hv_r*.csv $LATEX/$DATA
done


# update repo
cd $LATEX
git pull
git add $DATA
git commit -m "Updated data."
git push
cd ..
