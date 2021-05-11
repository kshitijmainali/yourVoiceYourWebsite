import React, { Component } from 'react'
import axios from 'axios'



class Navbar extends Component {
    render() {
        return (
            <nav class="navbar navbar-expand-lg navbar-light bg-transparent">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01"
                    aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
                    <a class="navbar-brand" href="#" style={{ color: 'aliceblue' }}>
                        <h3>Your Voice Your Website</h3>
                    </a>
                    <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
                        <li class="nav-item active invisible">
                            <a class="nav-link" href="#" style={{ color: 'aliceblue' }}>Home <span class="sr-only">(current)</span></a>
                        </li>
                        <li class="nav-item invisible">
                            <a class="nav-link" href="#" style={{ color: 'aliceblue' }}>About Us</a>
                        </li>
                        <li class="nav-item invisible">
                            <a class="nav-link disabled" href="#" style={{ color: 'aliceblue' }}>Contact</a>
                        </li>
                        <li>
                            <button type="button" id="button" class="btn btn-success" data-toggle="modal" data-target="#exampleModal">
                                Speak UP
                        </button>
                        </li>

                        <canvas id="canvas">

                        </canvas>
                        <div class="wrapper">
                            <div class="container">
                                <button type="button" id="button" class="btn btn-success" data-toggle="modal" data-target="#exampleModal">
                                    Speak UP
                                </button>
                                <i class="fas fa-microphone"></i>
                            </div>


                            <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                                aria-hidden="true">
                                <div class="modal-dialog" role="document">
                                    <div class="modal-content">
                                        <div class="modal-header">
                                            <h5 class="modal-title" id="exampleModalLabel">Give Voice Command</h5>
                                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                                <span aria-hidden="true">&times;</span>
                                            </button>
                                        </div>
                                        <div class="modal-body">

                                        </div>
                                        <div class="modal-footer">
                                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                            <button type="button" class="btn btn-primary">See changes</button>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </ul>
                </div>
            </nav>
        )
    }
}


class NewCommand extends Component {
    render() {
        return (
            <div>
                <div>
                    <Navbar />
                    <div class="wrapper">
                        <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
                            aria-hidden="true">
                            <div class="modal-dialog" role="document">
                                <div class="modal-content">
                                    <div class="modal-header">
                                        <h5 class="modal-title" id="exampleModalLabel">Give Voice Command</h5>
                                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                            <span aria-hidden="true">&times;</span>
                                        </button>
                                    </div>
                                    <div class="modal-body">

                                    </div>
                                    <div class="modal-footer">
                                        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                                        <button type="button" class="btn btn-primary">See changes</button>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <script src="js/style.js"></script>
                    </div>
                </div>
            </div>
        )
    }
}

export default NewCommand