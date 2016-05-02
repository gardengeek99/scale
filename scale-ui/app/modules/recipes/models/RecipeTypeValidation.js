(function () {
    'use strict';

    angular.module('scaleApp').factory('RecipeTypeValidation', function (RecipeTypeDefinition) {

        var getRecipeTypeValidationJobs = function (jobs) {
            var jobsOut = [];
            _.forEach(jobs, function(job){
               jobsOut.push({
                   recipe_inputs: job.recipe_inputs,
                   name: job.name,
                   job_type: {
                       name: job.job_type.name,
                       version: job.job_type.version
                   },
                   dependencies: job.dependencies
               })
            });
            return jobsOut;
        };
        
        var RecipeTypeValidation = function (id, name, version, title, description, input_data, jobs, trigger_rule) {
            if (id) {
                this.id = id;
            }
            this.name = name;
            this.version = version;
            this.title = title;
            this.description = description;
            this.input_data = input_data;
            this.jobs = getRecipeTypeValidationJobs(jobs);
            this.trigger_rule = trigger_rule;
        };

        // static methods, assigned to class
        RecipeTypeValidation.build = function (data) {
            if (data) {
                return new RecipeTypeValidation(
                    data.id,
                    data.name,
                    data.version,
                    data.title,
                    data.description,
                    data.input_data,
                    data.jobs,
                    data.trigger_rule
                );
            }
            return new RecipeTypeValidation();
        };

        RecipeTypeValidation.transformer = function (data) {
            if (angular.isArray(data)) {
                return data
                    .map(RecipeTypeValidation.build);
            }
            return RecipeTypeValidation.build(data);
        };

        return RecipeTypeValidation;
    });
})();