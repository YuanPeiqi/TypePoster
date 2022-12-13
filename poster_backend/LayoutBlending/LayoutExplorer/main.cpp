#include "LayoutExplorer.h"
#include <iostream>

int main(int argc, char *argv[])
{
    std::cout << "Initialize LayoutExplorer" << std::endl;
    LayoutExplorer le;
    std::string fileName0 = "..\\TestData\\template0.lay";
    std::string fileName1 = "..\\TestData\\template1.lay";
    le.OpenNextLayout(fileName0);
    le.OpenNextLayout(fileName1);
    le.Compute();
    std::vector<double> input_coefficient = { 0.0,0.25,0.5,0.75,1.0 };
    for (int i = 0; i < input_coefficient.size(); i++)
    {
        double alpha = input_coefficient[i];
        le.MovedAndCreate(alpha);
        le.SaveGenerLayout(alpha);
    }
    return 0;
}
