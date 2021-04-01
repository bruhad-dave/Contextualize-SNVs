repopath=`pwd`/scripts/

echo "Input folder: "
read inpath

echo "Output folder: "
read outpath

echo "Number of bins: "
read nbins

echo "Annotation file: "
read gtf_file
cd $outpath
for file in $inpath/*.txt
    do
        base=`basename $file _dedup.filt.genann.txt`
        echo $base
        /usr/local/bin/python3 $repopath/stack_genes_v4.py -n $nbins -i $file -s $base -a $gtf_file -o $outpath
        echo $base Done
    done

echo "Done, hopefully"
