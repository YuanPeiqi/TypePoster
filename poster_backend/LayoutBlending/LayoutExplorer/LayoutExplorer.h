#pragma once
#include <iostream>
#include "../Eigen/Core"
#include "../Eigen/Dense"
#include "CNodeMatching.h"
#include "CLayoutTree.h"
#include "CCompoundNode.h"
#include "CCompoundTree.h"
#include "CTransfer.h"

class LayoutExplorer
{
public:
	LayoutExplorer();
	~LayoutExplorer();
	//open each layout file
	void OpenNextLayout(std::string fileName);
	void Compute();
	void MovedAndCreate(double alpha);
	void SaveGenerLayout(double alpha, string outPath);
	void SaveLayoutAsSvg();
	void BatchCreateLay();

private:
	void CopyTree();
	void DeterInterVar(double slider_value);
	void SaveGenerLayoutForBatch(int order);
	void SetCompoundNodeLabel();
	void BatchSaveLayoutAsSvg(int order);
	int NodePresentTypeToInteger(CompoundNode* input_node);

private:
	Transfer layout_handler;
	CLayoutTree* m_firstLayout;
	CLayoutTree* m_secondLayout;

	CCompoundTree* combine_tree;
	CCompoundTree* combine_tree_copy;

	CompoundNode* comb_tree_root;
	CompoundNode* comb_tree_root_copy;

	std::vector<CLayoutTree*> m_uploadLayout;
};
