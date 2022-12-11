#include "LayoutExplorer.h"
#include <iostream>

int main(int argc, char *argv[])
{
    std::cout << "Initialize LayoutExplorer" << std::endl;
    LayoutExplorer le;
    std::string fileName = "..\\TestData\\183_layout.lay";
    le.OpenNextLayout(fileName);
    fileName = "..\\TestData\\981_layout.lay";
    le.OpenNextLayout(fileName);
    le.Compute();
    le.MovedAndCreate();
    le.SaveGenerLayout();
    return 0;
}
