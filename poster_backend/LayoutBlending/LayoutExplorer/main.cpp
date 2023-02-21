#include "LayoutExplorer.h"
#include <string>
#include<vector>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    assert(argc == 4);
    cout << "Initialize LayoutExplorer" << endl;
    LayoutExplorer le;
    string fileName0 = argv[1];
    string fileName1 = argv[2];
    string outPath = argv[3];
    le.OpenNextLayout(fileName0);
    le.OpenNextLayout(fileName1);
    le.Compute();
    vector<double> input_coefficient = { 0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0 };
    for (int i = 0; i < input_coefficient.size(); i++)
    {
        double alpha = input_coefficient[i];
        le.MovedAndCreate(alpha);
        le.SaveGenerLayout(alpha, outPath);
    }
    return 0;
}
