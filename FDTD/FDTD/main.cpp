#define _USE_MATH_DEFINES

#include <iostream>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

int L = 5;
int N = 200 * 2;                                                             // N doubled to simulate half steps
int iterNum = 800;
double deltaS = L / N;
double deltaT = (deltaS / N);
long double permitivity = 8.854 * pow(10, -6);								// vacuum permitivity
double permeability = 1.256; 								                // vacuum permeability
double conductivity = 10.1;                                                 // conductivity of steel

vector<double> E;
vector<double> H;
vector<double> tE;
//vector<double> tH;

int main()
{
    E.assign(N, 0);
    H.assign(N, 0);

    // applying instant current for testing purposes
    E[2] = 5;

    for(int i = 0; i < iterNum; i++) {
        // loop for values
        for (int n = 2; n < N; n = n+2) {
            H[n+1] = H[n-1] - permeability * E[n];
            E[n+2] = E[n] + permitivity * H[n+1];
        }

        // time graph
        tE.push_back(E[N]);
        //tH.push_back(H[N]);
    }

    cout << "\n\nx\n";

    // print x values
    for (int n = 0; n < iterNum; n++) {
        cout << to_string(n) + ",";
    }

    cout << "\n\ntE\n";

    // print E values
    for (int n = 0; n < iterNum; n++) {
        cout << to_string(tE[n]) + ",";
    }

//    cout << "\n\ntH\n";

//    // print H values
//    for (int n = 0; n < tH.size(); n++) {
//        cout << to_string(tH[n]) + ",";
//    }

}
