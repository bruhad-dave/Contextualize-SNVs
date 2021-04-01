repopath=`pwd`/scripts

echo "Input folder: "
read inpath

echo "Output folder: "
read outpath

echo "Flank Length "
read span

echo "Samtools path: `which samtools`"
samtools=`which samtools`

echo "Reference genome fasta file"
read ref_genome

pypath=`which python3`

cd $outpath
mkdir span_analysis
for file in $inpath/*.txt
    do
        base=`basename $file _dedup.filt.genann.txt`
        echo $base
        $pypath $repopath/get_span_v2.py -n $span -i $file -s $base
    done

for spans in $outpath/*.span_file.txt
    do
        basenew=`basename $spans .span_file.txt`
        echo $basenew
        $samtools faidx -r $spans $ref_genome > $basenew.spans.txt
    done


for sp_files in $outpath/*.spans.txt
    do
        basenext=`basename $sp_files .spans.txt`
        echo $basenext
        /usr/local/bin/python3 $repopath/span_analysis.py -i $sp_files -s $basenext -o ./span_analysis
    done

mkdir txt_files
mv $outpath/*.txt txt_files

echo "Done, hopefully"
