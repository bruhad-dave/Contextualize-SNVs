## collect arguments
while getopts i:o:r:d:f:t: flag
    do
        case "${flag}" in
            i ) inpath=${OPTARG} ;;
            o ) outpath=${OPTARG} ;;
            r ) rnacov=${OPTARG} ;;
            d ) dnacov=${OPTARG} ;;
            f ) freq=${OPTARG} ;;
            t ) input_type=${OPTARG} ;;
        esac
    done
#echo $inpath
#echo $outpath
#echo $rnacov
#echo $dnacov
#echo $freq
#echo $input_type

## making output folder if it does not exist
if [ -d "$outpath" ]
then
    echo "Directory already exists; continuing in $outpath" && cd $outpath
else
    mkdir $outpath && cd $outpath
fi

#commence with filtering
for data_file in $inpath/*.txt
    do
        echo $data_file
        base=`basename $data_file .txt`
        if [[ $input_type -eq 2 ]]
        then
            echo input files are annotated with DNA
            awk -F"\t" -v rnacov=$rnacov -v dnacov=$dnacov -v freq=$freq 'BEGIN {OFS = FS} {if ($5 >= rnacov && $9 >= freq && $10 >= dnacov && $13 == "-" && $8 != "-") print}' $data_file > $base-ann.filt.txt
        else
            echo input files are not annotated with DNA
            awk -F"\t" -v rnacov=$rnacov -v freq=$freq 'BEGIN {OFS = FS} {if ($5 >= rnacov && $9 >= freq && $8 != "-" && $6 >= 25) print}' $data_file > $base-filt.txt
        fi
    done

echo "Done, hopefully"
