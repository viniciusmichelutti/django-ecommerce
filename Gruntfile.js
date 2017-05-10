module.exports = function(grunt) {

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        concat: {
            app: {
                src: ['static/js/app/**/*.js'],
                dest: 'static/dist/js/app.js'
            },
            vendor: {
                src: ['static/js/vendor/**/*.js'],
                dest: 'static/dist/js/lib.js'
            }
        },

        uglify: {
            app: {
                files: {'static/dist/js/app.min.js': ['static/dist/js/app.js']}
            },
            vendor: {
                files: {'static/dist/js/lib.min.js': ['static/dist/js/lib.js']}
            }
        },

        less: {
            compile: {
                options: {
                    paths: ['static/less'],
                    compress: true
                },
                files: {
                    'static/dist/css/style.min.css': 'static/less/style.less'
                }
            }
        },

        watch: {
            less: {
                files: ['static/less/**/*.less'],
                tasks: ['less']
            }
        }
    });

    // Load plugins here.
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-watch');

    // Register tasks here.
    grunt.registerTask('default', ['concat', 'uglify', 'less']);
    grunt.registerTask('dev', ['concat', 'uglify', 'less', 'watch']);
};
