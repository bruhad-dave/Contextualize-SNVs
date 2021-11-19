## wraps around get_span_v2.py, samtools, and get_span_strcorr.py
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
        base=`basename $file _RNA-s2_dedup-filt.genann.txt`
        echo $base
        $pypath $repopath/get_span_v2.py -n $span -i $file -s $base
    done

for spans in $outpath/*.span_file.txt
    do
        basenew=`basename $spans .span_file.txt`
        echo $basenew
        $samtools faidx -r $spans $ref_genome | sed 's/>//g' | paste -d"\t" - - > $basenew.spans.txt
    done

for spanData in $outpath/*.spans.txt
    do
	spanbase=`basename $spanData .spans.txt`
	echo $spanbase
	$pypath $repopath/get_span_strcorr.py -i $spanData -d $spanbase.span_data_file.txt -n $spanbase
    done


for sp_files in $outpath/*.spans_strCorr.txt
    do
        basenext=`basename $sp_files .spans_strCorr.txt`
        echo $basenext
        $pypath $repopath/span_analysis_v2.py -i $sp_files -s $basenext -o ./span_analysis
    done

mkdir txt_files
mv $outpath/*.txt txt_files

echo "Done, hopefully"
