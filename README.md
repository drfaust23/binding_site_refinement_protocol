# binding_site_refinement_protocol
About binding site refinement protocol

본 문서는 단백질 binding site similarity 비교 프로그램인 [G-LoSA](https://compbio.lehigh.edu/GLoSA/)와 MD simulation package인 [OpenMM](www.openmm.org)을 이용해서 binding site refinement를 수행하는 방법에 관해서 설명한 문서입니다. 

본 문서에서 설명하는 내용은 "Ligand-Binding Site Structure Refinement Using Molecular Dynamics with Restraints Derived from Predicted Binding Site Templates" (J Chem Theory Comput. 2019 Nov 12; 15(11): 6524–6535) [Link](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6884403/)에서 설명된 과정을 따르고 있습니다. 
 
1. Finding similar binding site
모델 구조가 주어졌을 때, 우선 모델 단백질 구조와 유사한 리간드 결합 위치(ligand binding site)를 G-LoSA 프고그램을 이용해서 탐색해야한다. 이를 위해서 g-losa 프로그램을 [Link](https://compbio.lehigh.edu/GLoSA/)에서 다운 받는다. G-LoSA 프로그램은 단일 cpp 소스로 되어 있기 때문에 사용하는데 큰 무리는 없다 
일단 Arontier의 서버 내에는 다음 경로에 설치되어 있다. /Arontier/People/juyong/Project/binding_site_refinement/glosa_v2.2
