FROM maven:3.9.11-eclipse-temurin-21-alpine

WORKDIR /app

COPY pom.xml /app/
COPY src /app/src

RUN mvn clean package -DskipTests

EXPOSE 8080

# Run the Spring Boot application
CMD ["mvn", "spring-boot:run"]