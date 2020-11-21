//============================================================================
// Name        : FDTD2D.cpp
// Author      : Xhoni Robo
// Version     :
// Copyright   : None
// Description : FDSTD2D in C++
//============================================================================

#define _USE_MATH_DEFINES

#include <iostream>
#include <stdio.h>
#include <io.h>
#include <math.h>
#include <stdlib.h>
#include <cmath>
#include <vector>
#include <string>
#include <fstream>
#include <cstdarg>

using namespace std;

const double permitivity = 8.854e-12;												// vacuum permitivity
const double permeability = 1.256e-6; 								                // vacuum permeability

double L = 5;
int N = 200;
int iterNum = 400;
double deltaX = L / N;
double deltaY = L / N;
double deltaZ = L / N;
double deltaT = (deltaZ * sqrt(permitivity*permeability)  * (1/sqrt(2))); // 1/C * 1/sqrt2 * deltaZ

// variables needed for Gaussian Pulse excitation
double eps = 1e-3;
double Teps = 50 * deltaT;
double beta = -(pow((2/Teps), 2) * log(eps));


vector<vector<double>> Ex(N, vector<double> (N, 0));
vector<vector<double>> Ey(N, vector<double> (N, 0));
vector<vector<double>> Hz(N, vector<double> (N, 0));

const string filePath = "./Out/";

void writeEDataToCsvFile(string filename, vector<vector<double>> Ex, vector<vector<double>> Ey){

//	"x","y",Ex,Ey
//	0,0,Ex[x,y],Ey[x,y]

    ofstream csvFile(filename);
    csvFile << "x,y,z,Ex,Ey\n";

    for (int x = 0; x < Ex[0].size(); x++) {
    	for (int y = 0; y < Ex[x].size(); y++) {
    		csvFile << to_string(x) + "," + to_string(y) + ",0," + to_string(Ex[x][y]) + "," + to_string(Ey[x][y]) + "\n";
    	}
    }

    csvFile.close();
}

void writeHDataToCsvFile(string filename, vector<vector<double>> Hz){

//	"x","y",Hz
//	0,0,Hz[x,y]

    ofstream csvFile(filename);
    csvFile << "x,y,z,Hz\n";

    for (int x = 0; x < Hz[0].size(); x++) {
    	for (int y = 0; y < Ex[x].size(); y++) {
    		csvFile << to_string(x) + "," + to_string(y) + ",0," + to_string(Hz[x][y]) + "\n";
    	}
    }

    csvFile.close();
}

int main()
{
    for(int i = 0; i < iterNum; i++) {

    	double t = i * deltaT;
    	double gamma = Teps / 2;

    	// reducing the magnitude since in free space
        Hz[99][99] = exp(-(beta * pow((t - gamma), 2))) * 10e-4;  //TO-DO: Gaussian excitation, alpha = 1, Teps = 50*deltaT, eps = 1e-3, t = i * deltaT

        for (int i = 0; i < N-1; i++) {
        	for (int j = 1; j < N-2; j++) {
                Ex[i][j] = Ex[i][j] + (deltaT / permitivity / deltaZ) * (Hz[i][j] - Hz[i][j-1]);
        	}
        }

        for (int i = 1; i < N-2; i++) {
        	for (int j = 0; j < N-1; j++) {
                Ey[i][j] = Ey[i][j] - ((deltaT / permitivity / deltaZ) * (Hz[i][j] - Hz[i-1][j]));
        	}
        }

        writeEDataToCsvFile((filePath + "E/E.csv." + to_string(i)), Ex, Ey);

        // loop for values
        for (int i = 0; i < N-1; i++) {
        	for (int j = 0; j < N-1; j++) {
                Hz[i][j] = Hz[i][j] - ((deltaT / permeability / deltaZ) * (Ex[i][j] - Ex[i][j+1] + Ey[i+1][j] - Ey[i][j]));
        	}
        }


        writeHDataToCsvFile((filePath + "H/H.csv." + to_string(i)), Hz);

    }


}


