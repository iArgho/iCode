#include <iostream>
#include <string>

int main() {
    std::string name;
    int age;

    // Prompt for name and age
    std::cout << "Enter your name: ";
    std::getline(std::cin, name);  // Get full name with spaces

    std::cout << "Enter your age: ";
    std::cin >> age;

    // Output the collected information
    std::cout << "Hello, " << name << "!" << std::endl;
    std::cout << "You are " << age << " years old." << std::endl;

    return 0;
}