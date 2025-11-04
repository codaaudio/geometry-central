from conan import ConanFile


class GeometryCentralRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("eigen/[^3.3.9]")
        self.requires("nanoflann/[^1.6.0]")
        self.requires("nanort/cci.20251104")
        self.requires("happly/cci.20200822")

    def build_requirements(self):
        self.test_requires("gtest/1.17.0")
