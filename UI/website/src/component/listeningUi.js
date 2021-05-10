import React, { Component } from 'react'
import axios from 'axios'


class NewCommand extends Component {
    render() {
        return (
            <div>
                <canvas id="canvas">
                </canvas>
                <div class="wrapper">
                    {/* <!-- Button trigger modal --> */}
                    <div class="container">
                        <button type="button" id="button" class="btn btn-success" data-toggle="modal" data-target="#exampleModal">
                            Speak UP
                        </button>
                        <i class="fas fa-microphone"></i>
                    </div>
                    {/* <!-- Modal --> */}
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

                <script src="js/style.js"></script>
            </div>
        )
    }
}

export default NewCommand