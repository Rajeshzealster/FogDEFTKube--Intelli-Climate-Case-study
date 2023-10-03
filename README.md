# FogDEFTKube--Intelli-Climate-Case-study
# FogDEFTKube: An Extended FogDEFT Framework Supporting Kubernetes and Continuous Integration

## Project Overview

FogDEFTKube is an extended framework built upon the OASIS - Topology and Orchestration Specification for Cloud Applications (TOSCA) tailored for fog computing. This framework provides a user-friendly paradigm to model and dynamically deploy fog services remotely and on-demand. FogDEFTKube maintains four essential layers of abstraction:

1. **Platform Independence:** Utilizes Docker Containerization technology for seamless deployment across different platforms.
   ![Uploading Docker_host.png…]()


3. **Interoperability:** Leverages Kubernetes features to establish seamless inter-service communication and orchestration.

4. **Portability:** Incorporates TOSCA, a vendor-neutral modeling language, ensuring flexibility and compatibility with various cloud providers.
   ![Orchestration](https://github.com/Rajeshzealster/FogDEFTKube--Intelli-Climate-Case-study/assets/97143348/114be889-8810-45c9-a0ae-2e9eb6532256)


6. **CI/CD Integration:** Utilizes Jenkins server for continuous integration and deployment, enabling the automatic deployment of the latest code commits without human intervention.
   ![Uploading Jenkins_role.png…]()

## Key Features

- **TOSCA-Based Modeling**: Model fog services using TOSCA for clear and standardized representation.

- **Docker Containerization**: Achieve platform independence and efficient deployment using Docker containers.

- **Kubernetes Orchestration**: Leverage Kubernetes for scaling, load balancing, and managing containerized fog services.

- **Seamless Inter-Service Communication**: Enable communication and coordination between fog services within the Kubernetes cluster.

- **Continuous Integration and Deployment**: Automate the deployment process using Jenkins, ensuring rapid delivery of code changes.

## Prerequisites

Before getting started, ensure you have the following prerequisites in place:

1. **Kubernetes Cluster**: Set up a Kubernetes cluster where you intend to deploy fog services.

2. **Docker**: Install Docker on the target system to support containerization.

3. **TOSCA Modeling**: Familiarize yourself with TOSCA modeling concepts for fog service representation.

4. **Jenkins Server**: Have a Jenkins server configured for CI/CD integration.

## Contributing

If you would like to contribute to this project, please open an issue or submit a pull request. We welcome your contributions.


## Contact

For questions or feedback, feel free to contact the project maintainer:
- Rajesh Thalla - <rajeshzealster@gmail.com>
