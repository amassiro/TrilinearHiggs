# TrilinearHiggs

See here for the model:

    https://github.com/amassiro/HiggsTrilinear

    
Where:

    /afs/cern.ch/work/a/amassiro/Latinos/Framework/Combine/HiggsTrilinear/CMSSW_8_1_0/src/HiggsAnalysis/TrilinearHiggs

    
Run the model:
    
    text2workspace.py -m 125 datacard.txt -P HiggsAnalysis.TrilinearHiggs.HiggsTrilinear:higgsTrilinear  --PO=k_lambda,r  -o      model_test.root    

    DatacardMassiro_ttHOnly_v1.dat
    DatacardMassiro_ttHOnly_v2.dat
    
    
Running on the workspace (actual scanning of the k_lambda parameter):

    combine -M MultiDimFit model_test.root  --algo=grid --points 1000  -m 125   -t -1 --expectSignal=1     \
            --setParameterRanges k_lambda=-20,20:r=0.0,2.0       \
            --setParameters k_lambda=1,r=1     \
            --verbose -1

    combine -M MultiDimFit model_test.root  --algo=grid --points 100  -m 125   -t -1 --expectSignal=1     \
            --setParameterRanges k_lambda=-15,15:r=0.0,2.0       \
            --setParameters k_lambda=1,r=1     \
            --verbose -1

            
    combine -M MultiDimFit model_test.root  --algo=grid --points 9  -m 125   -t -1 --expectSignal=1     \
            --setParameterRanges k_lambda=-10,10:r=0.5,1.5       \
            --setParameters k_lambda=1,r=1     \
            --verbose -1

            
            
    combine -M MultiDimFit model_test.root  --algo=grid --points 300  -m 125   -t -1 --expectSignal=1     \
            --setParameterRanges k_lambda=-10,10:r=0.0,2.0       \
            --setParameters k_lambda=1,r=1     \
            --verbose -1

            
            
    combine -M MultiDimFit model_test.root  --algo=grid --points 120  -m 125   -t -1 --expectSignal=1     \
            --redefineSignalPOIs k_lambda --freezeParameters r --setParameters r=1    --setParameterRanges k_lambda=-20,20     \
            --verbose -1
        

        
        
    

    combineTool.py -d model_test.root -M MultiDimFit    \
               --algo=grid     --X-rtd OPTIMIZE_BOUNDS=0      -n "mytest2"   \
               --setParameterRanges k_lambda=-20,20:r=0.0,2.0       \
               --setParameters k_lambda=1,r=1     \
               --points 400    --job-mode lxbatch --task-name lxbatch-klmu-test2 --sub-opts='-q 8nm' --split-points 1 
                  
    ls -alrth higgsCombinemytest.POINTS.*.MultiDimFit.mH120.root  | grep -v 6.6K  | awk '{print "rm "$9}' | /bin/sh
    hadd higgsCombineLxbatch.root         higgsCombinemytest.POINTS.*.MultiDimFit.mH120.root

    ls -alrth higgsCombinemytest2.POINTS.*.MultiDimFit.mH120.root  | grep -v 6.6K  | awk '{print "rm "$9}' | /bin/sh
    hadd higgsCombineLxbatch2.root         higgsCombinemytest2.POINTS.*.MultiDimFit.mH120.root

    
    
    
    
    combine -M MultiDimFit model_test.root  --algo=grid --points 1000  -m 125    \
            --setParameterRanges k_lambda=-20,20:r=0.0,2.0       \
            --setParameters k_lambda=1,r=1     \
            --verbose -1
           
    
Draw:

    r99t higgsCombineTest.MultiDimFit.mH125.root  higgsCombineTest.MultiDimFit.mH125.root    draw.cxx
    r99t higgsCombineTest.MultiDimFit.mH125.root  higgsCombineTest.MultiDimFit.mH125.root    draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)

    r99t higgsCombineLxbatch.root higgsCombineLxbatch.root   draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)
    r99t higgsCombineLxbatch2.root higgsCombineLxbatch2.root   draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)

    r99t higgsCombineTest.MultiDimFit.mH125-signal1-tthonly.root   higgsCombineTest.MultiDimFit.mH125-signal1-tthonly.root    draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)

    
    r99t higgsCombineTest.MultiDimFit.mH125.VH.tth.root   higgsCombineTest.MultiDimFit.mH125.VH.tth.root    draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)

    r99t higgsCombineTest.MultiDimFit.mH125.VH.tth.small.root   higgsCombineTest.MultiDimFit.mH125.VH.tth.small.root    draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)
    
    
    
    