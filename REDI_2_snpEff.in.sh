echo "Enter path to input directory (containing REDItools output tables)."
read inpath

echo "Enter path to output directory."
read outpath

if [ -d "$outpath" ]
then
    echo "Directory already exists; continuing in $outpath" && cd $outpath
else
    mkdir $outpath && cd $outpath
fi

for data_file in $inpath/*.txt
    do
        base=`basename $data_file .txt`
        echo $data_file
        awk -F"\t" 'BEGIN {OFS = FS} {print $1,$2,"hit_"$1":"$2,$3,$8,$6}' $data_file > $base-snpEff.in.txt
    done

for raw_file in $outpath/*.txt
    do
        echo $raw_file
        sed -i ".bcp" "s/AG/G/g; s/AT/T/g; s/AC/C/g; s/TA/A/g; s/TG/G/g; s/TC/C/g; s/GA/A/g; s/GT/T/g; s/GC/C/g; s/CA/A/g; s/CT/T/g; s/CG/G/g; s/ /,/g" $raw_file
    done

rm $outpath/*.bcp

echo "Done, hopefully"
