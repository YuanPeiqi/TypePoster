#include "LayoutExplorer.h"
#include <string>
#include<vector>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    cout << argv[0] << argv[1] << endl;
    assert(argc == 3);
    cout << "Initialize LayoutExplorer" << endl;
    LayoutExplorer le;
    string fileName0 = argv[1];
    string fileName1 = argv[2];
    le.OpenNextLayout(fileName0);
    le.OpenNextLayout(fileName1);
    le.Compute();
    vector<double> input_coefficient = { 0.0, 0.25, 0.5, 0.75, 1.0 };
    for (int i = 0; i < input_coefficient.size(); i++)
    {
        double alpha = input_coefficient[i];
        le.MovedAndCreate(alpha);
        le.SaveGenerLayout(alpha);
    }
    return 0;
}
