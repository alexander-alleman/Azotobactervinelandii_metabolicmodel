# Azotobactervinelandii_metabolicmodel
Genome scale metabolic model describing aerobic nitrogen fixation in *Azotobacter vinelandii* 

<p>&nbsp;</p>

This is the corresponding model curation and analysis to the manuscript *Metabolic Model of the Nitrogen-Fixing Obligate AerobeAzotobacter vinelandiiPredicts Its Adaptation to OxygenConcentration and Metal Availability.* Found at: https://journals.asm.org/doi/10.1128/mBio.02593-21

<p>&nbsp;</p>



![membrane](./Notebooks/Images/Fullmodel.png)


<p>&nbsp;</p>

**Abstract:**
There is considerable interest in promoting biological nitrogen fixation (BNF) as a mechanism to reduce the inputs of nitrogenous fertilizers in agriculture, but considerable fundamental knowledge gaps still need to be addressed. BNF is catalyzed by nitrogenase, which requires a large input of energy in the form of ATP and low potential electrons. Diazotrophs that respire aerobically have an advantage in meeting the ATP demands of BNF but face challenges in protecting nitrogenase from inactivation by oxygen. Here, we constructed a genome-scale metabolic model of the nitrogen-fixing bacterium Azotobacter vinelandii, which uses a complex respiratory protection mechanism to consume oxygen at a high rate to keep intracellular conditions microaerobic. Our model accurately predicts growth rate under high oxygen and substrate concentrations, consistent with a large electron flux directed to the respiratory protection mechanism. While a partially decoupled electron transport chain compensates for some of the energy imbalance under high-oxygen conditions, it does not account for all substrate intake, leading to increased maintenance rates. Interestingly, the respiratory protection mechanism is required for accurate predictions even when ammonia is supplemented during growth, suggesting that the respiratory protection mechanism might be a core principle of metabolism and not just used for nitrogenase protection. We have also shown that rearrangement of flux through the electron transport system allows A. vinelandii to adapt to different oxygen concentrations, metal availability, and genetic disruption, which cause an ammonia excretion phenotype. Accurately determining the energy balance in an aerobic nitrogen-fixing metabolic model is required for future engineering approaches.

<p>&nbsp;</p>

**Importance:**
The world’s dependence on industrially produced nitrogenous fertilizers has created a dichotomy of issues. First, parts of the globe lack access to fertilizers, leading to poor crop yields that significantly limit nutrition while contributing to disease and starvation. In contrast, abundant nitrogenous fertilizers and associated overuse in large agricultural systems result in compromised soil quality and downstream environmental issues. Thus, there is considerable interest in expanding the impacts of BNF to promote improved crop yields in places struggling with access to industrial fertilizers while reducing fertilizer input in areas where overuse results in the degradation of soil health. A more robust and fundamental understanding of BNF biochemistry and microbial physiology will enable strategies to promote new and more robust associations between nitrogen-fixing microorganisms and crop plants.es.


## Organization of repository 
This repository has three folders Data, Notebooks, and Outputs

**Data:** contains all models, input and analysis data, and eshcher maps. 

**Notebooks:** contains all analysis files in the form of jupyter notebooks or figure production in python scripts. 

**Outputs:** mostly figures and graphs from anaylsis in low resolution. Also contains Memote reports. 

Model data was received from Tec-Campos et al. (
https://doi.org/10.1016/j.mec.2020.e00132) and corresponding github (https://github.com/cristalzucsd/AvinelandiiDJ) or received from the BiGG Model database

Experimental data from: Kuhla and Oelze, 1988, [Dependency of growth yield, maintenance and Ks-values on the dissolved oxygen concentration in continuous cultures of <i>Azotobacter vinelandii</i>](./Data/Experimental_Data/Khula_Oelze.pdf)

**Fair Warning, I am a biologist self taught in python scripting so I know there are faster ways of doing things. So feel free to use some of this for your own model just know there always is a better way!** 
