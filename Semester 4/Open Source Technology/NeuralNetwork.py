import numpy as np
import pandas as pd
from sklearn import preprocessing as pp
import matplotlib.pyplot as plt
import seaborn as sns


def load_dataset(filename):
    dataset = pd.read_csv(filename)
    description_of_data(dataset)
    return dataset


def description_of_data(data):
    print("Dataset info...")
    print(data.info())
    print()
    print("\nDataset description...")
    print(data.describe())
    print()
    print("\nNumber of differnt outputs...")
    print(data.groupby("species").size())
    print()


def loadingData(filename):
    min_max_scaler = pp.MinMaxScaler()
    data = load_dataset(filename)
    columns = data.columns[:-1]
    output_class_names = data.species.unique()
    target = data[["species"]].replace(output_class_names, [0, 1, 2])
    # noramalizing column values between 0 and 1
    data_normalize = pd.DataFrame(min_max_scaler.fit_transform(data[columns]))
    main_df = pd.concat([data_normalize, target], axis=1)
    return main_df


# Creating X_train, y_train
def split_dataset(dataFrame):
    '''
    Create a train and test dataset
    inputs -> {
        dataFrame : dataFrame created after loading the data
    }
    '''
    train_test_per = 80/100.0
    # creating training partition
    dataFrame['train'] = np.random.rand(len(dataFrame)) < train_test_per
    train = dataFrame[dataFrame.train == 1]
    train = train.drop("train", axis=1)
    # Creating testing partition
    test = dataFrame[dataFrame.train == 0]
    test = test.drop('train', axis=1)
    return train, test


def create_dataset_array(dataFrame):
    '''
    Creates a X and y columns
    X -> Features to be used for prediction
    y -> Column to predict
    inputs -> {
        dataFrame : train or test data frame
    }
    '''
    X = dataFrame.values[:, :4]
    targets = targets = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    y = np.array([targets[int(x)] for x in dataFrame.values[:, 4]])
    return X, y

# taken from> https://gist.github.com/craffel/2d727968c3aaebd10359


def draw_neural_net(ax, left, right, bottom, top, layer_sizes):
    '''
    Draw a neural network cartoon using matplotilb.

    :usage:
        >>> fig = plt.figure(figsize=(12, 12))
        >>> draw_neural_net(fig.gca(), .1, .9, .1, .9, [4, 7, 2])

    :parameters:
        - ax : matplotlib.axes.AxesSubplot
            The axes on which to plot the cartoon (get e.g. by plt.gca())
        - left : float
            The center of the leftmost node(s) will be placed here
        - right : float
            The center of the rightmost node(s) will be placed here
        - bottom : float
            The center of the bottommost node(s) will be placed here
        - top : float
            The center of the topmost node(s) will be placed here
        - layer_sizes : list of int
            List of layer sizes, including input and output dimensionality
    '''
    n_layers = len(layer_sizes)
    v_spacing = (top - bottom)/float(max(layer_sizes))
    h_spacing = (right - left)/float(len(layer_sizes) - 1)
    # Nodes
    for n, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing*(layer_size - 1)/2. + (top + bottom)/2.
        for m in range(layer_size):
            circle = plt.Circle((n*h_spacing + left, layer_top - m*v_spacing), v_spacing/4.,
                                color='w', ec='k', zorder=4)
            ax.add_artist(circle)
    # Edges
    for n, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing*(layer_size_a - 1)/2. + (top + bottom)/2.
        layer_top_b = v_spacing*(layer_size_b - 1)/2. + (top + bottom)/2.
        for m in range(layer_size_a):
            for o in range(layer_size_b):
                line = plt.Line2D([n*h_spacing + left, (n + 1)*h_spacing + left],
                                  [layer_top_a - m*v_spacing, layer_top_b - o*v_spacing], c='k')
                ax.add_artist(line)
    plt.show()


class NeuralNetwork(object):
    ''''
    Creates a 3 layer neural network
    Layers : input, hidden, output
    Inputs -> {
        num_inputs           : number of features in input
        hidden_layer_neurons : number of nodes in hidden layer
        num_outputs          : number of output classes
    }
    '''

    def __init__(self, num_inputs, hidden_layer_neurons, num_outputs):
        self.num_inputs = num_inputs
        self.hidden_layer_neurons = hidden_layer_neurons
        self.num_outputs = num_outputs
        # Weights for layers; values between -1 and 1
        # w1 weight mapping from Input nodes -->> Hidden nodes
        self.w1 = 2*np.random.random((self.num_inputs, self.hidden_layer_neurons)) - 1
        # w1 weight mapping from Input nodes -->> Hidden nodes
        self.w2 = 2*np.random.random((self.hidden_layer_neurons, self.num_outputs)) - 1

    def train(self, X, y, epochs=50000, learning_rate=0.001):
        ''''
        Training the neural Neural Network
        inputs -> {
            X             : Features
            y             : labels
            epochs        : No. of training cycles, default:50000
            learning rate : step size, default: 0.001
        }
        '''
        self.learning_rate = learning_rate
        for epoch in range(epochs):
            self.feedForward(X, y)
            self.backPropagation(X, y)
            if epoch % 10000 == 0:
                acc, err, _ = self.predict(X, y)
                print(f"Epoch: {epoch}/{epochs} Error: {self.error:.2f} Accuracy: {acc*100:.2f}%")
        acc, err, _ = self.predict(X, y)
        print(f"Epoch: {epochs}/{epochs} Error: {self.error:.2f} Accuracy: {acc*100:.2f}%")

    def feedForward(self, inputs, targets):
        '''
        Forward Propagation ( use current weights to caluculate output ):
        > node activation = output from previous layer (network inputs in case of first layer) * weights
        > node output = sigmoid activation function = 1 / ( 1 + exp( node                                                       activation ) )
        '''
        self.a1 = 1/(1 + np.exp(-(np.dot(inputs, self.w1))))
        self.ouput = 1/(1 + np.exp(-(np.dot(self.a1, self.w2))))
        self.error = (abs(targets - self.ouput)).mean()
        return self.ouput, self.error

    def backPropagation(self, X, y):
        '''
        Backpropagation ( update network weights ):
        Error calculation ( how far off we are from the expected values ):
        > derivative (different for different activation functions) = output *  ( 1 - output )
        > error (for the last layer) = ( expected - output ) * derivative
        > error (for other layers) = ( error calulated previously * that layer's                               weight ) * derivative
        Update weight based on error caculated:
        > Weight = weight + ( output * error * learning rate )
        '''
        ouput_delta = (y - self.ouput) * (self.ouput * (1 - self.ouput))
        a1_delta = ouput_delta.dot(self.w2.T) * (self.a1 * (1 - self.a1))
        self.w2 = self.w2 + self.a1.T.dot(ouput_delta) * self.learning_rate
        self.w1 = self.w1 + X.T.dot(a1_delta) * self.learning_rate

    def predict(self, X, y):
        output, err = self.feedForward(X, y)
        predicted = np.argmax(np.round(output, 3), axis=1)
        result = predicted == np.argmax(y, axis=1)
        correct = np.sum(result)/len(result)
        return correct, err, predicted

    def label_predicted(self, data, predicted):
        label_prediction = data[['species']].replace(
            [0, 1, 2], ['setosa', 'versicolor', 'virginica'])
        label_prediction['Predicted'] = predicted
        label_prediction['Predicted'] = label_prediction['Predicted'].replace(
            [0, 1, 2], ['setosa', 'versicolor', 'virginica'])
        data.drop("species", axis=1, inplace=True)
        data = pd.concat([data, label_prediction], axis=1)
        return data.iloc[:, 4:]


if __name__ == "__main__":
    np.random.seed(47)
    # displaying information about the data and data cleansing
    main_df = loadingData("Iris.csv")
    train, test = split_dataset(main_df)  # Dataframes
    X_train, y_train = create_dataset_array(train)  # numpy arrays
    X_test, y_test = create_dataset_array(test)

    iris = sns.load_dataset("iris")
    iris.boxplot(by="species", figsize=(12, 8))
    plt.show()

    # simple visualization to show how the inputs compare against each other
    columns = list(iris.columns.tolist()[:-1])
    # print(columns)
    sns.pairplot(data=iris, vars=tuple(columns), hue='species')
    plt.show()

    print("Sizes")
    print(f"X_train size: {len(X_train)}")
    print(f"Y_train size: {len(y_train)}")
    print(f"X_test size:  {len(X_test)}")
    print(f"Y_test size:  {len(y_test)}\n")

    num_inputs = len(X_train[0])
    hidden_layer_neurons = 5
    num_outputs = len(y_train[0])

    # creating network
    nn = NeuralNetwork(num_inputs, hidden_layer_neurons, num_outputs)
    print("Training Network...")
    fig = plt.figure(figsize=(12, 12))
    ax = fig.gca()
    ax.axis('off')
    plt.title("Neural Network architecture")
    draw_neural_net(ax, .1, .9, .1, .9, [4, hidden_layer_neurons, 3])

    # training network
    nn.train(X_train, y_train)
    # input("\nTesting network....")
    print("Testing network....")
    score, err, predicted = nn.predict(X_test, y_test)
    print(f"Accuracy: {score*100:.2f}%")
    print(f"Error: {err:.2f}%")
    print(nn.label_predicted(test, predicted))
    # input()
