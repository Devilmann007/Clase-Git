cmake_minimum_required(VERSION 3.10)
project(ProyectoMongoDB)

set(CMAKE_CXX_STANDARD 17)

# Ruta donde instalaste el driver C++ de MongoDB
set(CMAKE_PREFIX_PATH "C:/mongo-cxx-driver-install")

# Buscar los paquetes
find_package(libmongocxx REQUIRED)
find_package(libbsoncxx REQUIRED)

# Crear el ejecutable
add_executable(ProyectoMongoDB src/main.cpp)

# Incluir headers
target_include_directories(ProyectoMongoDB PRIVATE
    ${libmongocxx_INCLUDE_DIRS}
    ${libbsoncxx_INCLUDE_DIRS}
)

# Enlazar librerías
target_link_libraries(ProyectoMongoDB PRIVATE
    ${libmongocxx_LIBRARIES}
    ${libbsoncxx_LIBRARIES}
)