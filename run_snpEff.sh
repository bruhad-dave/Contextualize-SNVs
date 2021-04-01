echo "Enter path to snpEff: "
read sE_path

echo "Input folder: "
read inpath

echo "Output path: "
read outpath

if [ -d "$outpath" ]
then
    echo "Directory already exists; continuing in $outpath" && cd $outpath
else
    mkdir $outpath && cd $outpath
fi

for file in $inpath/*.filt-snpEff.in.txt
    do
        base=`basename $file .filt-snpEff.in.txt`
        #mkdir $outpath/$base
        echo $file
        `which java` -jar $sE_path/snpEff.jar PF3D7_41 $file > $outpath/$base.sEout.ann.vcf ## change PF3D7_41 to the correct reference code for the organism you're analysing
        for html in $outpath/snpEff_summary.html
            do
                htmlbase=`basename $html .html`
                mv $html $base.$htmlbase.html
            done
        for txt in $outpath/snpEff_genes.txt
            do
                txtbase=`basename $txt .txt`
                mv $txt $base.$txtbase.txt
            done
    done

echo "Done, hopefully"
