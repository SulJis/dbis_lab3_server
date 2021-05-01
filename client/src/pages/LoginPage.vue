<template>
    <main class="form-signin container text-center">
        <form>
            <h1 class="h3 mb-3 fw-normal">Please sign in {{ msg }}</h1>

            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                <label for="floatingInput">Email address</label>
            </div>
            <div class="form-floating">
                <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                <label for="floatingPassword">Password</label>
            </div>

            <div class="checkbox mb-3">
                <label>
                    <input type="checkbox" value="remember-me"> Remember me
                </label>
            </div>
            <button class="w-100 btn btn-lg btn-primary" type="submit">Sign in</button>
            <p class="mt-5 mb-3 text-muted">&copy; 2017–2021</p>
        </form>
    </main>
</template>

<script>
    import axios from "axios";
    export default {
        name: 'LoginPage',
        data(){
            return{
                msg: ""
            }
        },
        methods: {
            getMessage(){
                const path = "http://localhost:5000/login";
                axios.get(path)
                .then((res) => {
                    this.msg = res.data;
                })
                .catch((error) => {
                    console.error(error);
                });
            },
        },
        created(){
            this.getMessage();
        }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    main{
        width: 20%;

    }
</style>
