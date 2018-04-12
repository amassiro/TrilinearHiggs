# TrilinearHiggs

See here for the model:

    https://github.com/amassiro/HiggsTrilinear


    
Run the model:
    
    text2workspace.py -m 125 datacard.txt -P HiggsAnalysis.TrilinearHiggs.HiggsTrilinear:higgsTrilinear  --PO=k_lambda,r  -o      model_test.root    

Running on the workspace (actual scanning of the k_lambda parameter):

    combine -M MultiDimFit model_test.root  --algo=grid --points 1000  -m 125   -t -1 --expectSignal=1     \
            --setParameterRanges k_lambda=-20,20:r=0.0,2.0       \
            --setParameters k_lambda=1,r=1     \
            --verbose -1

            
    combine -M MultiDimFit model_test.root  --algo=grid --points 120  -m 125   -t -1 --expectSignal=1     \
            --redefineSignalPOIs k_lambda --freezeParameters r --setParameters r=1    --setParameterRanges k_lambda=-20,20     \
            --verbose -1
        
            
            
            
            
            --freezeParameters=r    \
            --verbose -1

Draw:

    r99t higgsCombineTest.MultiDimFit.mH125.root  higgsCombineTest.MultiDimFit.mH125.root    draw.cxx
    r99t higgsCombineTest.MultiDimFit.mH125.root  higgsCombineTest.MultiDimFit.mH125.root    draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)


    
    