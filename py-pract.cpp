#include <iostream>
using namespace std;

// Class
class Car {
public:
    string brand;

    void showBrand() {
        cout << "Car Brand: " << brand << endl;
    }
};

int main() {
    // Creating an instance (object) of the Car class
    Car car1;

    // Assigning a value to the object's data member
    car1.brand = "Toyota";

    // Calling the object's member function
    car1.showBrand();

    return 0;
}