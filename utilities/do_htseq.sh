## wraps around htseq to calculate intron and exon coverage for each sample
while getopts o:i:r: flag
    do
        case "${flag}" in
            o ) out_path=${OPTARG} ;;
            i ) input_dir_path=${OPTARG} ;;
            r ) ref_gff=${OPTARG} ;;
        esac
    done

if [ -d "$out_path" ]
then
    echo "Directory already exists; continuing in $out_path" && cd $out_path
else
    mkdir $out_path && cd $out_path
fi

for file in $input_dir_path/*.bam
    do
        filename=`basename $file .bam`
        echo $filename
        echo "Getting intron data..."
        htseq-count -q -t intron -s reverse -i Parent $file $ref_gff > $filename.intron.txt
        echo "Introns done, getting exon data..."
        htseq-count -q -t exon -s reverse -i Parent $file $ref_gff > $filename.exon.txt
        echo "Exons done."
    done

echo "Done, hopefully"
