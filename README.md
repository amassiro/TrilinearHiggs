# TrilinearHiggs

See here for the model:

    https://github.com/amassiro/HiggsTrilinear

    
Where:

    /afs/cern.ch/work/a/amassiro/Latinos/Framework/Combine/HiggsTrilinear/CMSSW_8_1_0/src/HiggsAnalysis/TrilinearHiggs

    
Run the model:
    
    text2workspace.py -m 125 datacard.txt -P HiggsAnalysis.TrilinearHiggs.HiggsTrilinear:higgsTrilinear  --PO=k_lambda,r  -o      model_test.root    
    text2workspace.py        datacard.txt -P HiggsAnalysis.TrilinearHiggs.HiggsTrilinear:higgsTrilinear  --PO=k_lambda,r  -o      model_test.root    

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
    
    combine -M MultiDimFit model_test.root  --algo=grid --points 10  -m 125   -t -1 --expectSignal=1     \
            --redefineSignalPOIs k_lambda --freezeParameters r --setParameters r=1    --setParameterRanges k_lambda=-20,20     \
            --verbose -1
    
    
    combine -M MultiDimFit model_test.root  --algo=grid --points 10  -m 125   -t -1 --expectSignal=1     \
            --redefineSignalPOIs r --freezeParameters k_lambda --setParameters k_lambda=1    --setParameterRanges r=0,2     \
            --verbose -1
    

    
    combineTool.py -M MultiDimFit  -d model_test.root  --algo=grid --points 10  -m 125   -t -1 --expectSignal=1     \
            --redefineSignalPOIs k_lambda --freezeParameters r --setParameters r=1    --setParameterRanges k_lambda=-20,20     \
            --verbose -1 --job-mode lxbatch --task-name lxbatch-klmu --sub-opts='-q 8nm' --split-points 1   -n "mytest2" 

    hadd higgsCombineLxbatchmytest2.root         higgsCombinemytest2.POINTS.*.MultiDimFit.mH125.root

    r99t higgsCombineLxbatchmytest2.root  higgsCombineLxbatchmytest2.root    draw.cxx


    
    

    
    
    
    
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    combineTool.py -M MultiDimFit  -d model_test.root  --algo=grid --points 400  -m 125   -t -1 --expectSignal=1     --X-rtd OPTIMIZE_BOUNDS=0   \
            --setParameters r=1:k_lambda=1    --setParameterRanges k_lambda=-20,20:r=-4.0,4.0       \
            --verbose -1 --job-mode lxbatch --task-name lxbatch-klmu --sub-opts='-q 8nm' --split-points 2   -n "my2D" 

    hadd higgsCombineLxbatchmy2D.root         higgsCombinemy2D.POINTS.*.MultiDimFit.mH125.root

    r99t higgsCombineLxbatchmy2D.root  higgsCombineLxbatchmy2D.root   draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)
    r99t higgsCombineLxbatchmy2D_itstrangelyworks.root  higgsCombineLxbatchmy2D_itstrangelyworks.root    draw.cxx


    
    
    combineTool.py -M MultiDimFit  -d model_test.root  --algo=grid --points 1000  -m 125   -t -1 --expectSignal=1     --X-rtd OPTIMIZE_BOUNDS=0   \
            --setParameters r=1:k_lambda=1    --setParameterRanges k_lambda=-150,150:r=-4.0,4.0       \
            --verbose -1 --job-mode condor --task-name condor-klmu  --split-points 4   -n "my2Dcondor" 

    hadd higgsCombineLxbatchmy2D.root         higgsCombinemy2Dcondor.POINTS.*.MultiDimFit.mH125.root

    r99t higgsCombineLxbatchmy2D.root  draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)

    ls -alrth higgsCombinemy2Dcondor.POINTS.*.MultiDimFit.mH125.root  | grep -v 6.6K  | grep -v 6.7K  | awk '{print "rm "$9}' | /bin/sh

    
    
    
    
    
    combineTool.py -M MultiDimFit  -d model_test.root  --algo=grid --points 400  -m 125     --X-rtd OPTIMIZE_BOUNDS=0   \
            --setParameters r=1:k_lambda=1    --setParameterRanges k_lambda=-20,20:r=-4.0,4.0      \
            --verbose -1 --job-mode condor --task-name condor-klmu  --split-points 2   -n "my2DcondorObs" 

    hadd higgsCombineLxbatchmy2DObs.root         higgsCombinemy2DcondorObs.POINTS.*.MultiDimFit.mH125.root

    r99t higgsCombineLxbatchmy2DObs.root   draw2D.cxx\(\"#mu\",\"k_\{#lambda\}\",\"r\",\"k_lambda\"\)

    
    
    
    combineTool.py -M MultiDimFit  -d model_test.root  --algo=grid --points 400  -m 125   -t -1 --expectSignal=1     --X-rtd OPTIMIZE_BOUNDS=0   \
            --setParameters r=1:k_lambda=1    --setParameterRanges k_lambda=-50,50      \
            --redefineSignalPOIs k_lambda      --freezeParameters r   \
            --verbose -1 --job-mode condor --task-name condor-kl  --split-points 2   -n "my1Dklcondor" 

            
    hadd higgsCombineLxbatchmy1Dklcondor.root         higgsCombinemy1Dklcondor.POINTS.*.MultiDimFit.mH125.root

    r99t higgsCombineLxbatchmy1Dklcondor.root  higgsCombineLxbatchmy1Dklcondor.root   draw.cxx

    

    
    
    
    
    combineTool.py -M MultiDimFit  -d model_test.root  --algo=grid --points 400  -m 125   -t -1 --expectSignal=1     --X-rtd OPTIMIZE_BOUNDS=0   \
            --setParameters r=1:k_lambda=1    --setParameterRanges r=-5,5      \
            --redefineSignalPOIs r      --freezeParameters k_lambda   \
            --verbose -1 --job-mode condor --task-name condor-mu  --split-points 2   -n "my1Dmucondor" 

            
    hadd higgsCombineLxbatchmy1Dmucondor.root         higgsCombinemy1Dmucondor.POINTS.*.MultiDimFit.mH125.root

    r99t higgsCombineLxbatchmy1Dmucondor.root  higgsCombineLxbatchmy1Dmucondor.root   draw.cxx

            
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    
    
    
    
    

    combineTool.py -d model_test.root -M MultiDimFit   -t -1 --expectSignal=1    \
               --algo=grid     --X-rtd OPTIMIZE_BOUNDS=0      -n "mytest2"   \
               --setParameterRanges k_lambda=-20,20:r=0.0,2.0       \
               --setParameters k_lambda=1,r=1     \
               --points 400    --job-mode lxbatch --task-name lxbatch-klmu-test2 --sub-opts='-q 8nm' --split-points 1 
                  
    ls -alrth higgsCombinemytest.POINTS.*.MultiDimFit.mH120.root  | grep -v 6.6K  | awk '{print "rm "$9}' | /bin/sh
    hadd higgsCombineLxbatch.root         higgsCombinemytest.POINTS.*.MultiDimFit.mH120.root

    ls -alrth higgsCombinemytest2.POINTS.*.MultiDimFit.mH120.root  | grep -v 6.6K  | awk '{print "rm "$9}' | /bin/sh
    hadd higgsCombineLxbatch2.root         higgsCombinemytest2.POINTS.*.MultiDimFit.mH120.root

    
    
    combineTool.py -d model_test.root -M MultiDimFit   -t -1 --expectSignal=1    \
               --algo=grid     --X-rtd OPTIMIZE_BOUNDS=0      -n "mytest1d"   \
               --setParameterRanges k_lambda=-20,20       \
               --redefineSignalPOIs k_lambda --freezeParameters r --setParameters r=1 \
               --points 200    --job-mode lxbatch --task-name lxbatch-klmu-1d --sub-opts='-q 8nm' --split-points 1 

               
    hadd higgsCombineLxbatchmytest1d.root         higgsCombinemytest1d.POINTS.*.MultiDimFit.mH120.root

    r99t higgsCombineLxbatchmytest1d.root  higgsCombineLxbatchmytest1d.root    draw.cxx
               
 
 
 
 
    combineTool.py -d model_test.root -M MultiDimFit   -t -1 --expectSignal=1    \
               --algo=grid     --X-rtd OPTIMIZE_BOUNDS=0      -n "mytest1dJust1D"   \
               --setParameterRanges k_lambda=-20,20       \
               --setParameters k_lambda=-4,r=1     \
               --redefineSignalPOIs k_lambda --freezeParameters r \
               --points 200    --job-mode lxbatch --task-name lxbatch-klmu-1d --sub-opts='-q 8nm' --split-points 1 

               
    hadd higgsCombineLxbatchmytest1dJust1D.root         higgsCombinemytest1dJust1D.POINTS.*.MultiDimFit.mH120.root

    r99t higgsCombineLxbatchmytest1dJust1D.root  higgsCombineLxbatchmytest1dJust1D.root    draw.cxx
               
    combine -M MultiDimFit model_test.root  --algo=grid --points 100  -m 125   -t -1 --expectSignal=1     \
            --setParameterRanges k_lambda=-20,20       \
            --setParameters k_lambda=-4,r=1     \
            --redefineSignalPOIs k_lambda --freezeParameters r \
            --verbose -1
    
    
    
    

    combineTool.py -d model_test.root -M MultiDimFit   -t -1   \
               --algo=grid     --X-rtd OPTIMIZE_BOUNDS=0      -n "mytest1dJust1Dmu"   \
               --setParameterRanges r=0,2       \
               --setParameters k_lambda=1,r=1     \
               --redefineSignalPOIs r --freezeParameters k_lambda \
               --points 100    --job-mode lxbatch --task-name lxbatch-klmu-1d-mu --sub-opts='-q 8nm' --split-points 1 

               
    combineTool.py -d model_test.root -M MultiDimFit   -t -1 --expectSignal=1    \
               --algo=grid     --X-rtd OPTIMIZE_BOUNDS=0      -n "mytest1dJust1Dmu"   \
               --setParameterRanges r=0,2       \
               --setParameters r=1     \
               --redefineSignalPOIs r \
               --points 100    --job-mode lxbatch --task-name lxbatch-klmu-1d-mu --sub-opts='-q 8nm' --split-points 1 
               
               
    hadd higgsCombineLxbatchmytest1dJust1Dmu.root         higgsCombinemytest1dJust1Dmu.POINTS.*.MultiDimFit.mH120.root


    r99t higgsCombineLxbatchmytest1dJust1Dmu.root  higgsCombineLxbatchmytest1dJust1Dmu.root    draw.cxx
    
    
               
               
               
    
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
    
    
    
    