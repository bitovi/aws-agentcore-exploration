package com.bitovi.repka_lite;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestBody;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

@Controller
public class HelloWorldController {

    @GetMapping(value = "/ping", produces = {
            MediaType.TEXT_HTML_VALUE })
    ResponseEntity<String> health() {
        return new ResponseEntity<>("ok", HttpStatus.OK);
    }

    @PostMapping(value = "/invocations", produces = {
            MediaType.APPLICATION_JSON_VALUE })
    ResponseEntity<InvacationRequestOutput> invocations(@RequestBody InvocationRequestInput body) {

        InvacationRequestOutput response = new InvacationRequestOutput(
                new Output(new Message("assistant",
                        new Content[] { new Content("Hello " + body.input.prompt) }),
                        String.valueOf(System.currentTimeMillis())));

        return new ResponseEntity<InvacationRequestOutput>(response, HttpStatus.OK);
    }

    private record InvocationRequestInput(Input input) {

    }

    private record Input(String prompt) {

    }

    private record InvacationRequestOutput(Output output) {

    }

    private record Output(Message message, String timestamp) {

    }

    private record Message(String role, Content[] content) {

    }

    private record Content(String text) {

    }

}
