from HiggsAnalysis.CombinedLimit.PhysicsModel import *
from HiggsAnalysis.CombinedLimit.SMHiggsBuilder import SMHiggsBuilder
import ROOT, os

class HiggsTrilinear(PhysicsModel):

#
# standard, not touched
#

    "Float independently cross sections and branching ratios"
    def __init__(self):
        PhysicsModel.__init__(self) # not using 'super(x,self).__init__' since I don't understand it
        self.mHRange = []
        self.poiNames = []

    def setPhysicsOptions(self,physOptions):
        for po in physOptions:
            if po.startswith("higgsMassRange="):
                self.mHRange = po.replace("higgsMassRange=","").split(",")
                if len(self.mHRange) != 2:
                    raise RuntimeError, "Higgs mass range definition requires two extrema"
                elif float(self.mHRange[0]) >= float(self.mHRange[1]):
                    raise RuntimeError, "Extrema for Higgs mass range defined with inverterd order. Second must be larger the first"

#
# standard, not touched (end)
#


#
# Define parameters of interest
#

    def doParametersOfInterest(self):
        """Create POI and other parameters, and define the POI set."""
        
        # trilinear Higgs couplings modified 
        self.modelBuilder.doVar("k_lambda[1,-50,50]")
        self.poiNames = "k_lambda"

        self.modelBuilder.doVar("r[1,-50,50]")
        self.poiNames += ",r"

        #
        # model: https://cp3.irmp.ucl.ac.be/projects/madgraph/wiki/HiggsSelfCoupling
        #
        
        #
        # N -->   N * ( 1 + z_0 * (k-1) ) = N * alpha(k)
        # with z_0 hardcoded for each bin of p_T Higgs
        #
        
        z0map = {
                 "hpt1":1.10,
                 "hpt2":0.30,
                 "hpt3":0.10,
                 "hpt4":0.03
                 }


        for proc in ["hpt1","hpt2","hpt3","hpt4"]: 
          alpha = z0map[proc]
          #self.modelBuilder.factory_("expr::XSscal_%s(\"1+(@0-1)*%g\",k_lambda)" % (proc,alpha))
          self.modelBuilder.factory_("expr::XSscal_%s(\"(1+(@0-1)*%g)*@1\",k_lambda,r)" % (proc,alpha))
        
        # make a dummy scaler of one ?
        #self.modelBuilder.doVar("ONE[1,1,1]")
        #self.modelBuilder.out.var("ONE").setConstant(True)

        print self.poiNames
        self.modelBuilder.doSet("POI",self.poiNames)




#
# Define how the yields change
#


    def getYieldScale(self,bin,process):

      if process in ["hpt1","hpt2","hpt3","hpt4"]: 
        return "XSscal_" + process
  
      else:
        return 1



higgsTrilinear = HiggsTrilinear()
