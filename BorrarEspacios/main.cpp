#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void crearFiles(string name, string extension=".txt", bool cerrarFile = false){
    ofstream myfile;
    myfile.open (name+extension);
    //myfile << "Writing this to a file.\n";
    if( cerrarFile) {
        myfile.close();
    }
}


int main()
{
   // crearFiles("myfile");
   /**  Abro file*/
    string STRING;
    ifstream infile;
	infile.open ("myfile.txt");

    ofstream correctFile;
    correctFile.open("correction.txt",);
        while(!infile.eof()) // To get you all the lines.
        {
	        getline(infile,STRING); // Saves the line in STRING.
	        //cout<<STRING<<" " ; // Prints our STRING.
	        correctFile<<STRING<<" ";
        }
	infile.close();
	correctFile.close();
    return 0;
}
